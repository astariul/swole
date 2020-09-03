def route_to_filename(route):
    """ Function to transform a route to a filename.

    Arguments:
        route (`str`): Route name to transform to a filename.

    Returns:
        `str`: Filename corresponding to the route.
    """
    return route.replace('/', '_')
