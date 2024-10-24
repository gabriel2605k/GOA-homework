def get_prime_numbers(lst):
    return [num for num in lst if is_prime(num)] # type: ignore
get_prime_numbers()