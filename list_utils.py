def unfold_list(list_of_lists, list_inside_list=None):
    """
    transforms a list of lists into a list of objects that were inside the lists
    :param list_of_lists: list of lobjects list
    :param list_inside_list: iterative list with objects
    :return: list with objects that are no longer lists
    """
    for obj in list_of_lists:

        if not isinstance(obj, list):
            list_inside_list.append(obj)
        else:
            unfold_list(obj, list_inside_list)
    return list_inside_list
