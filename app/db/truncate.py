from app.db.session import SessionLocal
from app.models.run_date import RunDate
from app.models.task import Task
from app.models.user import User

db = SessionLocal()


def truncate():
    db.query(RunDate).delete()
    db.query(Task).delete()
    db.query(User).delete()
    db.commit()


if __name__ == '__main__':
    confirmation = input('本当に実行してよろしいですか？（yesと入力）: ')
    if confirmation.lower() == 'yes':
        BOS = '\033[91m'  # 赤色表示用
        EOS = '\033[0m'

        print(f'{BOS}Truncating data...{EOS}')
        truncate()
    else:
        print('処理を中止しました。')
