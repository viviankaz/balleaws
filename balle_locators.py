from faker import Faker


step_4 = 'Physiotherapy Marketing Funnel - Step 4'
step_5 = 'Physiotherapy Marketing Funnel - Step 5'

step_4_url = 'https://seomarketingvancouverbc.ca/physiotherapy/booking/4/'
step_5_url = 'https://seomarketingvancouverbc.ca/physiotherapy/booking/7'

# fake = Faker(['it_IT', 'en_US', 'ja_JP', 'zh_CN', 'en_CA', 'fr_CA'])
fake = Faker('en_CA')

# Subject for painful problems message
subject = fake.sentence(nb_words=30)

# fake description
why = fake.catch_phrase()
#____________________Balle Media Funnel DATA PARAMETERS________________________________________
adv = 'Balle Media'
bmfunnel_url = 'https://seomarketingvancouverbc.ca/physiotherapy/get-started/?source_id=FB'
bm_home_page_title = 'Physiotherapy Marketing'

first_name = fake.first_name()
last_name = fake.last_name()
phone_number = fake.phone_number()
email = fake.email()
website = fake.domain_name()
area = fake.province_abbr()
subject = fake.sentence(10)
monthly_revenue = ['Less than $1,000 per month', '$1,001 - $5,000 per month', '$5,001 - $10,000 per month',
                   '$10,001 - $20,000 per month', '$20,001 - $50,000 per month', '$50,001 per month or more']


step_4 = 'Physiotherapy Marketing Funnel - Step 4'
step_5 = 'Physiotherapy Marketing Funnel - Step 5'

step_4_url = 'https://seomarketingvancouverbc.ca/physiotherapy/booking/4/'
step_5_url = 'https://seomarketingvancouverbc.ca/physiotherapy/booking/7'

# Subject for painful problems message
subject = fake.sentence(nb_words=30)

# fake description
why = fake.catch_phrase()
