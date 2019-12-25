import pymysql                                 # sqlite3 모듈 탑재
from Chapter17.select import select_all_books    # 데이터 조회용 함수 탑재


# 데이터 수정용 함수
def delete_books():
    try:
        conn = pymysql.connect(host='localhost', port=13306, user='root', passwd='root', db='bookstore', charset='utf8',
                             autocommit=False)
        cur = conn.cursor()  # 커서 확보

        # 데이터 삭제 SQL
        delete_sql = "delete from books where publisher = %s"

        # 삭제 SQL 실행
        cur.execute(delete_sql, 'A')

        conn.commit()                                   # 데이터베이스 반영
        print('데이터 삭제 건수]', cur.rowcount)
        print('[데이터 삭제 완료] ================== ')

    except:
        print ("예외 상황 발생")
        conn.rollback()                          # 데이터베이스 원복 (롤백)

    finally:
        conn.close()                                    # 커넥션 닫기

if __name__ == "__main__":		                # 외부에서 호출 시
    select_all_books()
    delete_books()                                  # 데이터 삭제 함수 호출
    select_all_books()
