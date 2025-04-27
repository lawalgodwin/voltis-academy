# project/app/middleware.py
import json
from django.http import JsonResponse


class StandardizeGraphQLResponseMiddleware:
    """
    Middleware to wrap all GraphQL JSON responses into a standardized format:
    {
        "status": "success" | "error",
        "data": {...} | null,
        "error": {...} | null
    }
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Only process JSON responses (e.g., GraphQL views return JSON by default)
        content_type = response.get('Content-Type', '')
        if 'application/json' in content_type:
            try:
                original = json.loads(response.content)
            except (ValueError, TypeError):
                # If parsing fails, return original
                return response

            # Build standardized payload
            standardized = {
                'status': 'error' if original.get('errors') else 'success',
                'data': original.get('data'),
                'error': original.get('errors')
            }
            # Return a fresh JsonResponse with the same status code
            return JsonResponse(
                data=standardized,
                status=response.status_code,
                safe=False
            )

        return response
