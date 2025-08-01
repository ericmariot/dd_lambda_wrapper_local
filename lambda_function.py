from typing import Any, Dict
import logging

from datadog_lambda.wrapper import datadog_lambda_wrapper

logger = logging.getLogger()
logger.setLevel(logging.INFO)

@datadog_lambda_wrapper
def lambda_handler(event: Dict[str, Any], context) -> Dict[str, Any]:
    logger.info("Processing event", extra={"event": event})
    
    print(f"Processing event: {event}")
    
    return {
        "statusCode": 200,
        "body": "Event processed successfully"
    }
