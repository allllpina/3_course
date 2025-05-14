# Lab 7 - fork/join*

from concurrent.futures import ThreadPoolExecutor

# ==== Сума частини списку ====
def partial_sum(numbers):
    print(f"Обчислення суми для підсписку: {numbers}")
    return sum(numbers)

# ==== Основна функція Fork/Join ====
def parallel_sum(data, num_parts=4):
    # Розбиваємо список на частини
    chunk_size = len(data) // num_parts
    chunks = [data[i * chunk_size: (i + 1) * chunk_size] for i in range(num_parts - 1)]
    chunks.append(data[(num_parts - 1) * chunk_size:])  # останній шматок
    
    with ThreadPoolExecutor() as executor:
        # fork — обчислюємо суми паралельно
        futures = [executor.submit(partial_sum, chunk) for chunk in chunks]
        
        # join — об'єднуємо результати
        total = sum(f.result() for f in futures)

    return total

# ==== Запуск ====

numbers = list(range(1, 1001))  # список від 1 до 1000
result = parallel_sum(numbers, num_parts=4)
print(f"\n🔢 Загальна сума: {result}")
