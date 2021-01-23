def combine_data(episode_number, episode_url, episode_description):
    number_list = []
    url_list = []
    title_list = []
    description_list = []

    for i in range(len(episode_number)):
        try:
            number_list.append(episode_number[i].text.strip())

            url_list.append(episode_url[i]['href'].strip('//'))

            title_list.append(episode_url[i].text)

            description_list.append(episode_description[i].text)
        except:
            print(f'There was a problem in the function while scraping')
            pass
    
    return number_list, url_list, title_list, description_list