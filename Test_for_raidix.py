# Тесты для "httpbin.org".
# Эндпоинты:
# "https://httpbin.org/headers",
# "https://httpbin.org/status/200",
# "https://httpbin.org/status/300",
# "https://httpbin.org/status/400",
# "https://httpbin.org/status/500".
# 
# Отчёт о тестировании генерируется в файл report.html посредством pytest-html
# с аргументами конфигурации "--html=report.html --self-contained-html".

import SetUp_for_tests as St


# Класс с тестами для эндпоинта "https://httpbin.org/headers".
class TestHttpbinHeadersPage:

    # Тест на соответствие статус кода в ответе коду 200.
    def test_headers_check_status_code_equals_200(self):
        assert St.headers_page_response.status_code == 200, "Код ответа не равен 200."

    # Тест на соответствие значения заголовка Content-Type формату JSON.
    def test_headers_check_content_type_equals_json(self):
        assert St.headers_page_response.headers["Content-Type"] \
               == "application/json", "Значение заголовка Content-Type не идентифицирует тело ответа как формат JSON."

    # Тест на соответствие значения заголовка Server требуемой версии: gunicorn/19.9.0.
    def test_headers_check_server_equals_required(self):
        assert St.headers_page_response.headers["Server"] == "gunicorn/19.9.0", "Тип сервера не идентифицируется как " \
                                                                                "требеумый: gunicorn/19.9.0"

    # Тест на соответствие значения Host в теле headers значению "httpbin.org".
    def test_headers_check_host_equals_httpbin_org(self):
        assert St.headers_page_response_body["headers"]["Host"] \
               == "httpbin.org", "Значение Host не соответствует 'httpbin.org'"

    # Тест на соответствие значения Accept в теле headers значению "*/*".
    def test_headers_check_accept_equals_required(self):
        assert St.headers_page_response_body["headers"]["Accept"] == "*/*"

    # Тест на соответствие значения Accept-Encoding в теле headers значению "gzip, deflate".
    def test_headers_check_accept_encoding_equals_gzip_deflate(self):
        assert St.headers_page_response_body["headers"]["Accept-Encoding"] == "gzip, deflate"

    # Тест на соответствие значения User-Agent в теле headers значению "python-requests/2.27.1".
    def test_headers_check_user_agent_equals_python_requests(self):
        assert St.headers_page_response_body["headers"]["User-Agent"] == "python-requests/2.27.1"


# Класс с тестами для эндпоинтов "https://httpbin.org/status/статус_код".
class TestHttpbinStatusCodePages:

    # Тест на соответствие статус кода в ответе коду 200.
    def test_code_200_check_equals_200(self):
        assert St.code_200_page_response.status_code == 200, "Код ответа не равен 200."

    # Тест на соответствие статус кода в ответе коду 300.
    def test_code_300_check_equals_300(self):
        assert St.code_300_page_response.status_code == 300, "Код ответа не равен 300."

    # Тест на соответствие статус кода в ответе коду 400.
    def test_code_400_check_equals_400(self):
        assert St.code_400_page_response.status_code == 400, "Код ответа не равен 400."

    # Тест на соответствие статус кода в ответе коду 500.
    def test_code_200_check_equals_500(self):
        assert St.code_500_page_response.status_code == 500, "Код ответа не равен 500."
