import pymysql

# 데이터 입력 함수
def insert_books():
    try:
        conn = pymysql.connect(host='localhost', port=13306, user='root', passwd='root', db='bookstore', charset='utf8',
                             autocommit=False)
        cur = conn.cursor()
        # 데이터 입력 SQL
        insert_sql = """INSERT INTO books (title, published_date, publisher, pages, recommendation) 
                            VALUES (%s, %s, %s, %s, %s)"""

        # 튜플을 이용한 데이터 입력
        cur.execute(insert_sql, ('클린 코드', '2010.03.04','B', 584, 1))

        # 책의 정보를 담고 있는 튜플들의 리스트
        books = [
            ('개발자의 코드', '2013.02.28','A', 200, 0),
            ('빅데이터 마케팅', '2014.07.02','A', 296, 1),
            ('구글드', '2010.02.10','B', 526, 0),
            ('강의력', '2013.12.12','A', 248, 1)
        ]

        # 여러 데이터 입력
        cur.executemany(insert_sql, books)
        conn.commit()       # 데이터베이스 반영
        print('[데이터 입력 완료] ================== ')

    except:
        print ("예외 상황 발생")
        conn.rollback()                          # 데이터베이스 원복 (롤백)

    finally:
        conn.close()        # 커넥션 닫기

if __name__ == "__main__":		# 외부에서 호출 시
    insert_books()                  # 데이터 입력 함수 호출
