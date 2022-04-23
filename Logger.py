from datetime import datetime

RED = "\033[91m"
BLUE = "\033[94m"
RESET = "\033[0m"
GREEN = "\033[92m"
ORANGE = '\033[33m'

class Logger:
	def getTime():
		return datetime.now().strftime("%H:%M:%S")

	def info(reason):
		print(f"[{Logger.getTime()}] {BLUE}{reason}{RESET}")
		pass

	def warning(reason):
		print(f"[{Logger.getTime()}] {ORANGE}{reason}{RESET}")

	def error(reason):
		print(f"[{Logger.getTime()}] {RED}{reason}{RESET}")
		pass

	def success(message):
		print(f"[{Logger.getTime()}] {GREEN}{message}{RESET}")

	def debug(message):
		print(f"[{Logger.getTime()}] {ORANGE}{message}{RESET}")
