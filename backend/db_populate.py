from app import services

def run():
    services.populate_db()

if __name__ == '__main__':
    run()
    print("done.")