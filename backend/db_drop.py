from app import api, db, services

def run():
    services.drop_db()

if __name__ == '__main__':
    run()
    print("done.")