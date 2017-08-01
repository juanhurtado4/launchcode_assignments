def get_country_codes(prices):
    string = prices[0:2]
    for n in range(len(prices)):
        if prices[n] == ' ':
            string = string + ',' + ' ' + prices[n+1:n+3]
            
    return string

get_country_codes('GZ2343, CD2323, JS2323')
            
            
