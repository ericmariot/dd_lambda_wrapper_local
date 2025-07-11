FROM public.ecr.aws/lambda/python:3.12

COPY --from=public.ecr.aws/datadog/lambda-extension:82 /opt/. /opt/

COPY requirements.txt .
RUN pip install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

COPY app/ ${LAMBDA_TASK_ROOT}/app/
COPY lambda_function.py ${LAMBDA_TASK_ROOT}/

ENV DD_SITE=datadoghq.com
ENV DD_TRACE_ENABLED=True
ENV DD_API_KEY=your_api_key
ENV DD_LOG_LEVEL=debug

CMD ["lambda_function.lambda_handler"]
