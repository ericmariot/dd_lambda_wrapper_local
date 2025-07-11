from typing import Any, Dict

from datadog_lambda.wrapper import datadog_lambda_wrapper


@datadog_lambda_wrapper
def lambda_handler(event: Dict[str, Any], context) -> Dict[str, Any]:
    print("Processing event: %s", event)
    return
