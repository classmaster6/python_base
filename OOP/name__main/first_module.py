print(f"First module's name: {__name__}")


def main():
	print("Run directly")

def imported():
	print("Run from import")


if __name__ == '__main__':
	main()
else:
	imported()