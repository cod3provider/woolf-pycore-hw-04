def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        total = 0
        count = 0

        for line in lines:
            name, salary = line.strip().split(',')
            total += int(salary)
            count += 1

        if count == 0:
            raise ValueError("The file is empty")

        average = total / count
        return total, average

    except FileNotFoundError:
        print(f"Error: The file at path '{path}' was not found.")
        return None, None
    except ValueError as ve:
        print(f"Error: {ve}")
        return None, None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None, None



total, average = total_salary("01_salaries.txt")
if total is not None and average is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
