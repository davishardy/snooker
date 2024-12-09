""" Find all the render files """

from pathlib import Path
import subprocess

show_folder = Path("/home/dhardy/mount/CollaborativeSpace/inkwashed/show")
BLENDER_PATH = "/opt/blender/blender"

def find_files(prefix):
    """
    Finds all .blend files that should be rendered
    Inputs:
        prefix = show prefix
    Outputs:
        list of paths to files
    """
    render_files = []

    shot_folders = show_folder.glob(f"{prefix}*")
    for shot in shot_folders:
        blend_files = shot.glob(f"{prefix}*.blend")
        for blend_file in blend_files:
            render_files.append(blend_file)

    return render_files


def render_file(input_file, start, end):
    """
    Executed a command line render
    Inputs:
        input_file = path to file you want to render
        start = start frame
        end = end frame
    Outputs:
        None
    """
    file_path = f"{input_file.parent / input_file.stem}.####.exr"

    args = [
        BLENDER_PATH,
        "-b",
        input_file,
        "-E",
        "BLENDER_EEVEE_NEXT",
        "-s",
        str(start),
        "-e",
        str(end),
        "-F",
        "OPEN_EXR_MULTILAYER",
        "-o",
        file_path,
        "-a"
    ]

    subprocess.run(args, check=True)
