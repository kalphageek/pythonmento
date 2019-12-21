#import sqlite3  # SQLite3 탑재
import pymysql


# 테이블 생성용 함수
def create_table():
    try
        #conn = sqlite3.connect('my_books.db')  # 데이터베이스 커넥션 생성
        conn = pymysql.connect(host='localhost', port=13306, user='root', passwd='root', db='bookstore', charset='utf8',
                             autocommit=True)

        cur = conn.cursor()  # 커서 확보

        # my_books 테이블 생성
        cur.execute('''CREATE TABLE books (
                            id integer not null auto_increment,
                            title text,
                            published_date text,
                            publisher text,
                            pages integer,
                            recommendation integer,
                            primary key (id)
                    )'''
                    )

        conn.commit()       # 데이터베이스 반영

    finally:
        if conn:
            conn.close()        # 커넥션 닫기

if __name__ == "__main__":		               # 외부에서 호출 시
    create_table()          # 테이블 생성 함수 호출
