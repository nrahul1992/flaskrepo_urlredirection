from random import randint
from urllib import parse

__search_text__ = "######### Automated Entries Starts Here ##########"


def type1Handler(request):

    ticket_number = request.form.get('ticket_number')
    source_file_path = request.form.get('source_file_path')
    source_url = request.form.get('source_url')
    destination_url = request.form.get('destination_url')
    rule_preview = request.form.get('rule_preview')
    comments = request.form.get('comments')

    try:
        with open(source_file_path, 'r+', encoding='utf-8') as f:
            contents = f.read()
        f.close()
        if contents is not None and \
                __search_text__ in contents:

            searchStringIndex = contents.index(__search_text__) + __search_text__.__len__()
            first_part = contents[:searchStringIndex]
            second_part = contents[searchStringIndex+1:]
            redirect_rule = rulebuilder(source_url, destination_url)
            rule = "\n \n ####" + ticket_number + " starts here #### \n" + \
                    redirect_rule + \
                   " \n ####" + ticket_number + " ends here #### \n \n"
            entry_number = randint(10000, 99999)
            final_content = first_part + rule + second_part

            print(final_content + "\n entry number is ----", entry_number)
        else:
            return None
        with open(source_file_path, 'w', encoding='utf-8')as fi:
            fi.write(final_content)
        fi.close()
        return entry_number

    except FileNotFoundError as e:
        print("Exception occurred: " + e)


def rulebuilder(source, destination):

    country_codes = ["eut", "uk", "eu", "no", "sk", "se", "pl", "it", "ie", "fi", "cz",
                     "mt", "gr", "is", "at", "nl", "be", "lu", "hu", "fr", "es", "dk"]
    source_relative_path = parse.urlparse(source).path
    destination_relative_path = parse.urlparse(destination).path
    country_code = parse.urlparse(source).path.split("/")[1]
    if parse.urlparse(source).netloc == parse.urlparse(destination).netloc and \
            parse.urlparse(source).path.split("/")[1] == parse.urlparse(destination).path.split("/")[1]:
        while country_code in country_codes:
            redirect_rule = '<If $uri =~ \"^/' + country_code + '\" and $uri =~ \"(.*)' + source_relative_path +'(.*)\">' \
                            + '\n NameTrans fn=\"redirect\"  url=\"$1' + destination_relative_path + '\" status=\"301\"' \
                            + '</If>'

            return redirect_rule
    else:
        return None


def testMethod2():

    file_path = "C:\KiaMotors\preprod-configs\KME-obj - Copy.conf"
    search_text = "######### Automated Entries Starts Here ##########"
    insert_text = "\n test test  \n ... Just \t not testing! \n"

    with open(file_path, 'r+', encoding='utf-8') as f:
        contents = f.read()
    f.close()
    if search_text in contents:
        yup = "found"
        print('holy smokes it works')
        print(contents)
        r = contents.index(search_text) + search_text.__len__()
        print(r)
        first_part = contents[:r]
        second_part = contents[r+1:]
        final_content = first_part + insert_text + second_part
        print(final_content)

    else:
        yup = "not found"
        print("meh! ")

    with open(file_path, 'w', encoding='utf-8')as fi:
        fi.write(final_content)
    fi.close()
    return yup


