import os


class Constants:
    # Get the directory of the currently executing script (main.py)
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Navigate up two levels to the 'src' directory
    src_dir = os.path.abspath(os.path.join(script_dir, '..'))

    # Specify the path to the JSON file
    JSON_PATH = os.path.join(src_dir, 'src','Data', 'MemberList.json')

    RED_COLOR = "#D63D3D"
    RED_HOVER_COLOR = "#BC3535"

    GREEN_COLOR = "#36C170"
    GREEN_HOVER_COLOR = "#30A15F"

    BLUE_COLOR = "#409DBF"
    BLUE_HOVER_COLOR = "#327A94"