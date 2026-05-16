import time

class RequestLogMiddleware:
    def __init__(self, get_response):
        # Цей метод виконується один раз при запуску сервера
        self.get_response = get_response

    def __call__(self, request):
        # 1. Засікаємо час ПЕРЕД виконанням запиту
        start_time = time.time()

        # Передаємо запит далі (до в'юхи)
        response = self.get_response(request)

        # 2. Обчислюємо час ПІСЛЯ виконання
        duration = time.time() - start_time

        # 3. Виводимо в консоль метод, шлях і час
        # Форматуємо час до 3 знаків після коми
        print(f"[{request.method}] {request.path} - {duration:.3f}s")

        # 4. Додаємо кастомний заголовок у відповідь (Response)
        response['X-App-Name'] = 'MyDjangoApp'

        return response