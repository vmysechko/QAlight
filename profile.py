def create_profile(first: str, last: str, **user_info):
    """Function to create a vocabulary with users"""
    profile = {'first_name': first.title(), 'last_name': last.title()}
    for key, value in user_info.items():
        profile[key] = value
    return profile
