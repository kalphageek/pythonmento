import sqlite3                                      # sqlite3 모듈 탑재
from Chapter17.select import select_one_book        # 데이터 조회용 함수 탑재


# 데이터 수정용 함수
def update_books():
    # with문으로 컨택스트 관리 적용
    with sqlite3.connect('my_books.db') as conn:

        cur = conn.cursor()  # 커서 확보

        # 데이터 수정 SQL ( 제목이 ? 인 책의 추천 유무를 ? 로 변경하라 )
        update_sql = 'UPDATE my_books SET recommendation=? WHERE title=?'

        # 수정 SQL 실행
        cur.execute(update_sql, (1, '클린 코드'))

if __name__ == "__main__":		            # 외부에서 호출 시
    select_one_book()
    update_books()                                  # 데이터 수정 함수 호출
    print('[데이터 수정 완료] ================== ')
    select_one_book()