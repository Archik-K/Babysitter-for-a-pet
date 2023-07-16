from core import Config, app

__all__ = ["main"]


def main():
    app.run(debug=Config.DEBUG_MODE, host="0.0.0.0")


if __name__ == "__main__":
    main()
