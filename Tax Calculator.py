def federal_tax(cost):
    def calculate_tax(cost, tax):
        tax = cost * tax
        tax = round(tax, 2)
        return tax

    if cost <= 12550:
        return 0
    elif cost > 12550:
        tax = 9875 * 0.1
    
    if cost > 40125:
        tax += (40125 - 9875) * 0.12
    elif cost <= 40125:
        tax += calculate_tax(cost - 9875, 0.12)
        return tax
    
    if cost > 85525:
        tax += (85525 - 40125) * 0.22
    elif cost <= 85525:
        tax += calculate_tax(cost - 40125, 0.22)
        return tax
    
    if cost > 163300:
        tax += (163300 - 85525) * 0.24
    elif cost <= 163300:
        tax += calculate_tax(cost - 85525, 0.24)
        return tax
    
    if cost > 207350:
        tax += (207350 - 163300) * 0.32
    elif cost <= 207350:
        tax += calculate_tax(cost - 163300, 0.32)
        return tax
    
    if cost > 518400:
        tax += (518400 - 207350) * 0.35
    elif cost <= 518400:
        tax += calculate_tax(cost - 207350, 0.35)
        return tax

    if cost > 518400:
        tax += cost - 518400 * 0.37

    tax = round(tax, 2)
    return tax

#https://www.finansistas.net/npd.html
#https://www.tax.lt/skaiciuokles/atlyginimo_ir_mokesciu_skaiciuokle
#https://www.vmi.lt/evmi/en/gyventoju-pajamu-mokestis2
def lithuanian_tax(cost):
    if cost <= 730:
        #npd is non-taxable income
        npd = 460
        income_tax = (cost - npd) * 0.2
        health_tax = cost * 0.0698
        pention_tax = cost * 0.1252

        tax = income_tax + health_tax + pention_tax

        tax = round(tax, 2)
        return tax
    
    elif cost > 730 and cost <= 1678:
        npd = 460 - 0.26 * 730
        income_tax = (cost - npd) * 0.2
        health_tax = cost * 0.0698 
        pention_tax = cost * 0.1252 

        tax = income_tax + health_tax + pention_tax

        tax = round(tax, 2)
        return tax

    elif cost > 1678:
        npd = 400 - 0.18 * 642
        income_tax = (cost - npd) * 0.2
        health_tax = cost * 0.0698
        pention_tax = cost * 0.1252

        tax = income_tax + health_tax + pention_tax

        tax = round(tax, 2)
        return tax

    return 0

def british_taxes(cost):
    tax = 0

    if cost <= 12570:
        return 0
    elif cost > 12570:
        if cost > 50270:
            tax += (50270 - 12570) * 0.2
        elif cost <= 50270:
            tax += (cost - 12570) * 0.2
            tax = round(tax, 2)
            return tax
        
        if cost > 150000:
            tax += (150000 - 50270) * 0.4
        elif cost <= 150000:
            tax += (cost - 50270) * 0.4
            tax = round(tax, 2)
            return tax

        if cost > 150001:
            tax += (cost - 150000) * 0.45
        
        tax = round(tax, 2)
        return tax


def main():
    country = input('Enter your country: ')
    cost = float(input('Enter your monthly taxable income: '))

    #America
    if country.upper() == 'US' or country.upper() == 'USA' or country.upper() == 'UNITED STATES':
        tax = federal_tax(cost)
        print('Your federal income tax is:', tax, 'dollars')
        print('Total income with federal income tax deducted is:', round(cost - tax, 2), 'dollars')

    #Lithuania
    elif 'lit' in country.lower():
        tax = lithuanian_tax(cost)
        print('Your tax is:', tax, 'euros')
        print('Total income with tax deducted is:', round(cost - tax, 2), 'euros')

    #England
    elif 'eng' in country.lower() or 'uk' in country.lower():
        tax = british_taxes(cost)
        print('Your tax is:', tax, 'pounds')
        print('Total income with tax deducted is:', round(cost - tax, 2), 'pounds')
    
if __name__ == '__main__':
    main()
