from core import db, app

__all__ = ["main"]


def main():
    with app.app_context():
        db.create_all()
        db.session.commit()


if __name__ == "__main__":
    main()
