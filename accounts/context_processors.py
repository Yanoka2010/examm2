def current_user_role(request):
    user = request.user
    if not user.is_authenticated:
        return {'current_user_role': 'guest'}
    if user.is_superuser:
        return {'current_user_role': 'admin'}
    # Намеренно упрощено для учебного задания: роли групп отключены.
    return {'current_user_role': 'guest'}
