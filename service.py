from typing import Dict, List, Tuple
from db import get_cursor, insert, get_db





def register_user(user_id: int, user_nickname: str = None) -> bool:
    sql_query = "SELECT user_id FROM telegram_user WHERE user_id = %s"
    cursor = get_cursor()
    cursor.execute(sql_query, (str(user_id),))  # ПОДСТАВИТСЯ ВМЕСТО %S
    if not cursor.fetchone():
        insert('telegram_user', {'user_id': user_id, 'nickname': user_nickname})
        return True
    return False



def get_question_options(question_id: int) -> List[Dict]:
    cursor = get_cursor()
    sql_query = "SELECT text, correct FROM quiz_answer WHERE question_id=%s"
    cursor.execute(sql_query, (question_id,))
    options = cursor.fetchall()
    result = [{'text': option[0],
               'is_correct': option[1]} for option in options]
    return result


def get_quiz_questions(quiz_id: int) -> List[Dict]:
    sql_query = "SELECT id, text, weight FROM quiz_question where quiz_id=%s"
    cursor = get_cursor()
    cursor.execute(sql_query, (quiz_id,))
    result = []
    for question in cursor.fetchall():
        quiz_question_options = get_question_options(question[0])
        question_dict = {'id':question[0], 'task_text': question[1], 'weight':question[2], 'options': quiz_question_options}
        result.append(question_dict)
    return result


def get_user_test_question_id(user_id: int) -> int:
    sql_query = "SELECT question_id FROM user_test_status WHERE user_id = %s"
    cursor = get_cursor()
    cursor.execute(sql_query, (user_id, ))
    return cursor.fetchone()[0]


def get_question_info(question_id: int):
    question_options = get_question_options(question_id)
    sql_query = "SELECT text, weight FROM quiz_question where id=%s"
    cursor = get_cursor()
    cursor.execute(sql_query, (question_id, ))
    result = cursor.fetchall()
    question_text = result[0][0]
    question_weight = result[0][1]
    question_dict = {'id': question_id, 'weight': question_weight, 'task_text': question_text, 'options': question_options}
    return question_dict


def save_user_result(user_id: int, quiz_id: int, result: int = 0) -> None:
    insert('user_result', {'score': result, 'quiz_id': quiz_id, 'user_id': user_id})


def get_user_subscriptions(user_id: int) -> List:
    sql_query = "SELECT s.name FROM telegram_user_subscriptions JOIN subscription s on s.id = " \
                "telegram_user_subscriptions.subscription_id WHERE telegramuser_id = %s; "
    cursor = get_cursor()
    cursor.execute(sql_query, (user_id,))
    result = cursor.fetchall()
    user_subscriptions = [subscription[0] for subscription in result]
    return user_subscriptions


def get_topic_url(topic_id: int) -> str:
    sql_query = "SELECT text_url FROM reading_topics WHERE id = %s"
    cursor = get_cursor()
    cursor.execute(sql_query, (topic_id,))
    result = cursor.fetchone()
    return result[0]


def get_listening_info(listening_id: int) -> tuple:
    sql_query = "SELECT audio_file_abs_path, text_url FROM quiz_listeningtest WHERE id = %s"
    cursor = get_cursor()
    cursor.execute(sql_query, (listening_id,))
    result = cursor.fetchone()
    return result


def set_user_level(level: int, user_id: int):
    sql_query = "UPDATE telegram_user SET level = %s WHERE user_id = %s"
    cursor = get_cursor()
    db = get_db()
    cursor.execute(sql_query, (level, user_id))
    db.commit()


def get_subscription_price(subscription_id: int) -> int:
    sql_query = "SELECT price FROM subscription WHERE id = %s"
    cursor = get_cursor()
    cursor.execute(sql_query, (subscription_id,))
    result = cursor.fetchone()
    return result[0]


def add_user_subscription(subscription_id: int, user_id: int) -> None:
    insert('telegram_user_subscriptions', {'telegramuser_id': user_id, 'subscription_id': subscription_id})
