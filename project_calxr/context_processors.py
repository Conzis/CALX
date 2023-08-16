from app_general.views import calculate_BMR

def calculated_bmr_context(request):
    calculated_bmr_values = []

    latest_x = request.session.get('latest_x', None)
    if latest_x:
        calculated_bmr = calculate_BMR(latest_x)
        calculated_bmr_values.append(calculated_bmr)

    return {'calculated_bmr_values': calculated_bmr_values}