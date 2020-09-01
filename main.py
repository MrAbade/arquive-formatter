from io import TextIOWrapper

ACCOUNT_FILE_NAME = './accounts.txt'



def account_text_to_dict(account_text: str) -> dict:
    account_text = account_text.replace('{', '')
    account_text = account_text.replace('}', '')
    account_text = account_text.replace('"', '')
    
    account_list_malformatted = account_text.split(',')
    
    account_list = list()
    for item in account_list_malformatted:
        account_list.append(item.split(':')[1].replace('\n', ''))

    account_dict = dict()

    account_keys = ["id", 'conta', 'agencia', 'banco', 'cidade', 'estado']
    for i, key in enumerate(account_keys):
        account_dict[key] = account_list[i]
    
    return account_dict


def delete_duplicates(account_list: list) -> list:
    accounts_tuple = [tuple(account.items()) for account in account_list]
    account_list_without_duplicates_tuple = list(set(accounts_tuple))


    account_list_without_duplicates = [dict(account) for account in account_list_without_duplicates_tuple]

    return account_list_without_duplicates


def ids_in_ascending_order(account_list: list) -> list:
    account_list_in_ascending_order = []
    
    for id, account_dict in enumerate(account_list):
        account_dict["id"] = id
        account_list_in_ascending_order.append(account_dict)
    
    return account_list_in_ascending_order


def get_account(file: TextIOWrapper):
    new_line = file.readline()
    while new_line:
        yield new_line
        new_line = file.readline()


def get_account_list(file_name: str) -> list:
    with open(file_name, 'r+') as file:
        
        account_list = []
        for line in get_account(file):
            account_list.append(account_text_to_dict(line))
        return account_list

def main():
    account_list = get_account_list(ACCOUNT_FILE_NAME)
    account_list_without_duplicates = delete_duplicates(account_list)
    account_list_normalized = ids_in_ascending_order(account_list_without_duplicates)
    for line in account_list_normalized:
        print(line)


if __name__ == '__main__':
    main()
