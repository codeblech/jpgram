from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from datetime import datetime
import os


def index(request):
    return render(request, "base.html")


def cice_jiit(request):
    static_dir = os.path.join(
        settings.BASE_DIR, "magazine", "static", "magazine", "cice_jiit"
    )
    image_data_list = []
    if os.path.exists(static_dir):
        for filename in sorted(os.listdir(static_dir), reverse=True):
            if filename.endswith((".webp", ".jpg", ".jpeg", ".png")):
                image_path = f"magazine/cice_jiit/{filename}"
                datetime_str = filename.split("_UTC")[0]

                try:
                    image_datetime = datetime.strptime(
                        datetime_str, "%Y-%m-%d_%H-%M-%S"
                    )
                    formatted_datetime = image_datetime.strftime("%B %d, %Y")
                except ValueError:
                    formatted_datetime = "Unknown Date/Time"

                filename_without_ext = os.path.splitext(filename)[0]

                # Check for an extra numeric part after the UTC and remove it if present
                if filename_without_ext.endswith("_UTC"):
                    caption_filename = filename_without_ext + ".txt"
                else:
                    caption_filename = '_'.join(filename_without_ext.split('_')[:-1]) + ".txt"

                # Join with the static directory to get the full path
                caption_path = os.path.join(static_dir, caption_filename)

                caption = "No caption available"

                if os.path.exists(caption_path):
                    with open(caption_path, "r") as caption_file:
                        caption = caption_file.read().strip()

                image_data_list.append(
                    {
                        "image": image_path,
                        "caption": caption,
                        "datetime": formatted_datetime,
                    }
                )
                print(image_data_list)

    return render(
        request, "magazine/cice_jiit.html", {"image_data_list": image_data_list}
    )


def crescendojiit(request):
    static_dir = os.path.join(
        settings.BASE_DIR, "magazine", "static", "magazine", "crescendojiit"
    )

    image_data_list = []
    if os.path.exists(static_dir):
        for filename in sorted(os.listdir(static_dir), reverse=True):
            if filename.endswith((".webp", ".jpg", ".jpeg", ".png")):
                image_path = f"magazine/crescendojiit/{filename}"
                datetime_str = filename.split("_UTC")[0]

                try:
                    image_datetime = datetime.strptime(
                        datetime_str, "%Y-%m-%d_%H-%M-%S"
                    )
                    formatted_datetime = image_datetime.strftime("%B %d, %Y")
                except ValueError:
                    formatted_datetime = "Unknown Date/Time"

                filename_without_ext = os.path.splitext(filename)[0]

                # Check for an extra numeric part after the UTC and remove it if present
                if filename_without_ext.endswith("_UTC"):
                    caption_filename = filename_without_ext + ".txt"
                else:
                    caption_filename = '_'.join(filename_without_ext.split('_')[:-1]) + ".txt"

                # Join with the static directory to get the full path
                caption_path = os.path.join(static_dir, caption_filename)

                caption = "No caption available"

                if os.path.exists(caption_path):
                    with open(caption_path, "r") as caption_file:
                        caption = caption_file.read().strip()

                image_data_list.append(
                    {
                        "image": image_path,
                        "caption": caption,
                        "datetime": formatted_datetime,
                    }
                )
                print(image_data_list)

    return render(
        request, "magazine/crescendojiit.html", {"image_data_list": image_data_list}
    )


def gdscjiit(request):
    static_dir = os.path.join(
        settings.BASE_DIR, "magazine", "static", "magazine", "gdscjiit"
    )

    image_data_list = []
    if os.path.exists(static_dir):
        for filename in sorted(os.listdir(static_dir), reverse=True):
            if filename.endswith((".webp", ".jpg", ".jpeg", ".png")):
                image_path = f"magazine/gdscjiit/{filename}"
                datetime_str = filename.split("_UTC")[0]

                try:
                    image_datetime = datetime.strptime(
                        datetime_str, "%Y-%m-%d_%H-%M-%S"
                    )
                    formatted_datetime = image_datetime.strftime("%B %d, %Y")
                except ValueError:
                    formatted_datetime = "Unknown Date/Time"

                filename_without_ext = os.path.splitext(filename)[0]

                # Check for an extra numeric part after the UTC and remove it if present
                if filename_without_ext.endswith("_UTC"):
                    caption_filename = filename_without_ext + ".txt"
                else:
                    caption_filename = '_'.join(filename_without_ext.split('_')[:-1]) + ".txt"

                # Join with the static directory to get the full path
                caption_path = os.path.join(static_dir, caption_filename)

                caption = "No caption available"

                if os.path.exists(caption_path):
                    with open(caption_path, "r") as caption_file:
                        caption = caption_file.read().strip()

                image_data_list.append(
                    {
                        "image": image_path,
                        "caption": caption,
                        "datetime": formatted_datetime,
                    }
                )
                print(image_data_list)

    return render(
        request, "magazine/gdscjiit.html", {"image_data_list": image_data_list}
    )


def jaypee_photo_enthusiasts_guild(request):
    static_dir = os.path.join(
        settings.BASE_DIR,
        "magazine",
        "static",
        "magazine",
        "jaypee.photo.enthusiasts.guild",
    )

    image_data_list = []
    if os.path.exists(static_dir):
        for filename in sorted(os.listdir(static_dir), reverse=True):
            if filename.endswith((".webp", ".jpg", ".jpeg", ".png")):
                image_path = f"magazine/jaypee.photo.enthusiasts.guild/{filename}"
                datetime_str = filename.split("_UTC")[0]

                try:
                    image_datetime = datetime.strptime(
                        datetime_str, "%Y-%m-%d_%H-%M-%S"
                    )
                    formatted_datetime = image_datetime.strftime("%B %d, %Y")
                except ValueError:
                    formatted_datetime = "Unknown Date/Time"

                filename_without_ext = os.path.splitext(filename)[0]

                # Check for an extra numeric part after the UTC and remove it if present
                if filename_without_ext.endswith("_UTC"):
                    caption_filename = filename_without_ext + ".txt"
                else:
                    caption_filename = '_'.join(filename_without_ext.split('_')[:-1]) + ".txt"

                # Join with the static directory to get the full path
                caption_path = os.path.join(static_dir, caption_filename)

                caption = "No caption available"

                if os.path.exists(caption_path):
                    with open(caption_path, "r") as caption_file:
                        caption = caption_file.read().strip()

                image_data_list.append(
                    {
                        "image": image_path,
                        "caption": caption,
                        "datetime": formatted_datetime,
                    }
                )
                print(image_data_list)

    return render(
        request,
        "magazine/jaypee.photo.enthusiasts.guild.html",
        {"image_data_list": image_data_list},
    )


def jhankaarjiit(request):
    static_dir = os.path.join(
        settings.BASE_DIR, "magazine", "static", "magazine", "jhankaarjiit"
    )

    image_data_list = []
    if os.path.exists(static_dir):
        for filename in sorted(os.listdir(static_dir), reverse=True):
            if filename.endswith((".webp", ".jpg", ".jpeg", ".png")):
                image_path = f"magazine/jhankaarjiit/{filename}"
                datetime_str = filename.split("_UTC")[0]

                try:
                    image_datetime = datetime.strptime(
                        datetime_str, "%Y-%m-%d_%H-%M-%S"
                    )
                    formatted_datetime = image_datetime.strftime("%B %d, %Y")
                except ValueError:
                    formatted_datetime = "Unknown Date/Time"

                filename_without_ext = os.path.splitext(filename)[0]

                # Check for an extra numeric part after the UTC and remove it if present
                if filename_without_ext.endswith("_UTC"):
                    caption_filename = filename_without_ext + ".txt"
                else:
                    caption_filename = '_'.join(filename_without_ext.split('_')[:-1]) + ".txt"

                # Join with the static directory to get the full path
                caption_path = os.path.join(static_dir, caption_filename)

                caption = "No caption available"

                if os.path.exists(caption_path):
                    with open(caption_path, "r") as caption_file:
                        caption = caption_file.read().strip()

                image_data_list.append(
                    {
                        "image": image_path,
                        "caption": caption,
                        "datetime": formatted_datetime,
                    }
                )
                print(image_data_list)

    return render(
        request, "magazine/jhankaarjiit.html", {"image_data_list": image_data_list}
    )


def jiit_impressions(request):
    static_dir = os.path.join(
        settings.BASE_DIR, "magazine", "static", "magazine", "jiit.impressions"
    )

    image_data_list = []
    if os.path.exists(static_dir):
        for filename in sorted(os.listdir(static_dir), reverse=True):
            if filename.endswith((".webp", ".jpg", ".jpeg", ".png")):
                image_path = f"magazine/jiit.impressions/{filename}"
                datetime_str = filename.split("_UTC")[0]

                try:
                    image_datetime = datetime.strptime(
                        datetime_str, "%Y-%m-%d_%H-%M-%S"
                    )
                    formatted_datetime = image_datetime.strftime("%B %d, %Y")
                except ValueError:
                    formatted_datetime = "Unknown Date/Time"

                filename_without_ext = os.path.splitext(filename)[0]

                # Check for an extra numeric part after the UTC and remove it if present
                if filename_without_ext.endswith("_UTC"):
                    caption_filename = filename_without_ext + ".txt"
                else:
                    caption_filename = '_'.join(filename_without_ext.split('_')[:-1]) + ".txt"

                # Join with the static directory to get the full path
                caption_path = os.path.join(static_dir, caption_filename)

                caption = "No caption available"

                if os.path.exists(caption_path):
                    with open(caption_path, "r") as caption_file:
                        caption = caption_file.read().strip()

                image_data_list.append(
                    {
                        "image": image_path,
                        "caption": caption,
                        "datetime": formatted_datetime,
                    }
                )
                print(image_data_list)

    return render(
        request, "magazine/jiit.impressions.html", {"image_data_list": image_data_list}
    )


def jiityouthclub(request):
    static_dir = os.path.join(
        settings.BASE_DIR, "magazine", "static", "magazine", "jiityouthclub"
    )

    image_data_list = []
    if os.path.exists(static_dir):
        for filename in sorted(os.listdir(static_dir), reverse=True):
            if filename.endswith((".webp", ".jpg", ".jpeg", ".png")):
                image_path = f"magazine/jiityouthclub/{filename}"
                datetime_str = filename.split("_UTC")[0]

                try:
                    image_datetime = datetime.strptime(
                        datetime_str, "%Y-%m-%d_%H-%M-%S"
                    )
                    formatted_datetime = image_datetime.strftime("%B %d, %Y")
                except ValueError:
                    formatted_datetime = "Unknown Date/Time"

                filename_without_ext = os.path.splitext(filename)[0]

                # Check for an extra numeric part after the UTC and remove it if present
                if filename_without_ext.endswith("_UTC"):
                    caption_filename = filename_without_ext + ".txt"
                else:
                    caption_filename = '_'.join(filename_without_ext.split('_')[:-1]) + ".txt"

                # Join with the static directory to get the full path
                caption_path = os.path.join(static_dir, caption_filename)

                caption = "No caption available"

                if os.path.exists(caption_path):
                    with open(caption_path, "r") as caption_file:
                        caption = caption_file.read().strip()

                image_data_list.append(
                    {
                        "image": image_path,
                        "caption": caption,
                        "datetime": formatted_datetime,
                    }
                )
                print(image_data_list)

    return render(
        request, "magazine/jiityouthclub.html", {"image_data_list": image_data_list}
    )


def knuth_jiit(request):
    static_dir = os.path.join(
        settings.BASE_DIR, "magazine", "static", "magazine", "knuth_jiit"
    )

    image_data_list = []
    if os.path.exists(static_dir):
        for filename in sorted(os.listdir(static_dir), reverse=True):
            if filename.endswith((".webp", ".jpg", ".jpeg", ".png")):
                image_path = f"magazine/knuth_jiit/{filename}"
                datetime_str = filename.split("_UTC")[0]

                try:
                    image_datetime = datetime.strptime(
                        datetime_str, "%Y-%m-%d_%H-%M-%S"
                    )
                    formatted_datetime = image_datetime.strftime("%B %d, %Y")
                except ValueError:
                    formatted_datetime = "Unknown Date/Time"

                filename_without_ext = os.path.splitext(filename)[0]

                # Check for an extra numeric part after the UTC and remove it if present
                if filename_without_ext.endswith("_UTC"):
                    caption_filename = filename_without_ext + ".txt"
                else:
                    caption_filename = '_'.join(filename_without_ext.split('_')[:-1]) + ".txt"

                # Join with the static directory to get the full path
                caption_path = os.path.join(static_dir, caption_filename)

                caption = "No caption available"

                if os.path.exists(caption_path):
                    with open(caption_path, "r") as caption_file:
                        caption = caption_file.read().strip()

                image_data_list.append(
                    {
                        "image": image_path,
                        "caption": caption,
                        "datetime": formatted_datetime,
                    }
                )
                print(image_data_list)

    return render(
        request, "magazine/knuth_jiit.html", {"image_data_list": image_data_list}
    )


def nssjiit62(request):
    static_dir = os.path.join(
        settings.BASE_DIR, "magazine", "static", "magazine", "nssjiit62"
    )

    image_data_list = []
    if os.path.exists(static_dir):
        for filename in sorted(os.listdir(static_dir), reverse=True):
            if filename.endswith((".webp", ".jpg", ".jpeg", ".png")):
                image_path = f"magazine/nssjiit62/{filename}"
                datetime_str = filename.split("_UTC")[0]

                try:
                    image_datetime = datetime.strptime(
                        datetime_str, "%Y-%m-%d_%H-%M-%S"
                    )
                    formatted_datetime = image_datetime.strftime("%B %d, %Y")
                except ValueError:
                    formatted_datetime = "Unknown Date/Time"

                filename_without_ext = os.path.splitext(filename)[0]

                # Check for an extra numeric part after the UTC and remove it if present
                if filename_without_ext.endswith("_UTC"):
                    caption_filename = filename_without_ext + ".txt"
                else:
                    caption_filename = '_'.join(filename_without_ext.split('_')[:-1]) + ".txt"

                # Join with the static directory to get the full path
                caption_path = os.path.join(static_dir, caption_filename)

                caption = "No caption available"

                if os.path.exists(caption_path):
                    with open(caption_path, "r") as caption_file:
                        caption = caption_file.read().strip()

                image_data_list.append(
                    {
                        "image": image_path,
                        "caption": caption,
                        "datetime": formatted_datetime,
                    }
                )
                print(image_data_list)

    return render(
        request, "magazine/nssjiit62.html", {"image_data_list": image_data_list}
    )


def osdcjiit(request):
    static_dir = os.path.join(
        settings.BASE_DIR, "magazine", "static", "magazine", "osdcjiit"
    )

    # Collect all the image filenames
    image_data_list = []
    if os.path.exists(static_dir):
        for filename in sorted(os.listdir(static_dir), reverse=True):
            if filename.endswith((".webp", ".jpg", ".jpeg", ".png")):
                image_path = f"magazine/osdcjiit/{filename}"
                datetime_str = filename.split("_UTC")[0]

                try:
                    # Convert the extracted part to a datetime object
                    image_datetime = datetime.strptime(
                        datetime_str, "%Y-%m-%d_%H-%M-%S"
                    )
                    formatted_datetime = image_datetime.strftime("%B %d, %Y")
                except ValueError:
                    formatted_datetime = "Unknown Date/Time"

                # Try to find the corresponding caption (same name but with .txt extension)
                filename_without_ext = os.path.splitext(filename)[0]

                # Check for an extra numeric part after the UTC and remove it if present
                if filename_without_ext.endswith("_UTC"):
                    caption_filename = filename_without_ext + ".txt"
                else:
                    caption_filename = '_'.join(filename_without_ext.split('_')[:-1]) + ".txt"

                # Join with the static directory to get the full path
                caption_path = os.path.join(static_dir, caption_filename)

                # Default caption if no caption file exists
                caption = "No caption available"

                # Read caption from the file if it exists
                if os.path.exists(caption_path):
                    with open(caption_path, "r") as caption_file:
                        caption = (
                            caption_file.read().strip()
                        )  # Strip to remove any extra newlines

                # Append the image and its caption to the list
                image_data_list.append(
                    {
                        "image": image_path,
                        "caption": caption,
                        "datetime": formatted_datetime,
                    }
                )
                print(image_data_list)

    return render(
        request, "magazine/osdcjiit.html", {"image_data_list": image_data_list}
    )


def parola_literaryhub(request):
    static_dir = os.path.join(
        settings.BASE_DIR, "magazine", "static", "magazine", "parola.literaryhub"
    )

    # Collect all the image filenames
    image_data_list = []
    if os.path.exists(static_dir):
        for filename in sorted(os.listdir(static_dir), reverse=True):
            if filename.endswith((".webp", ".jpg", ".jpeg", ".png")):
                image_path = f"magazine/parola.literaryhub/{filename}"
                datetime_str = filename.split("_UTC")[0]

                try:
                    # Convert the extracted part to a datetime object
                    image_datetime = datetime.strptime(
                        datetime_str, "%Y-%m-%d_%H-%M-%S"
                    )
                    formatted_datetime = image_datetime.strftime(
                        "%B %d, %Y"
                    )
                except ValueError:
                    formatted_datetime = "Unknown Date/Time"

                # Try to find the corresponding caption (same name but with .txt extension)
                filename_without_ext = os.path.splitext(filename)[0]

                # Check for an extra numeric part after the UTC and remove it if present
                if filename_without_ext.endswith("_UTC"):
                    caption_filename = filename_without_ext + ".txt"
                else:
                    caption_filename = '_'.join(filename_without_ext.split('_')[:-1]) + ".txt"

                # Join with the static directory to get the full path
                caption_path = os.path.join(static_dir, caption_filename)

                # Default caption if no caption file exists
                caption = "No caption available"

                # Read caption from the file if it exists
                if os.path.exists(caption_path):
                    with open(caption_path, "r") as caption_file:
                        caption = (
                            caption_file.read().strip()
                        )  # Strip to remove any extra newlines

                # Append the image and its caption to the list
                image_data_list.append(
                    {
                        "image": image_path,
                        "caption": caption,
                        "datetime": formatted_datetime,
                    }
                )
                print(image_data_list)

    return render(
        request,
        "magazine/parola.literaryhub.html",
        {"image_data_list": image_data_list},
    )


def radiance_hub(request):
    static_dir = os.path.join(
        settings.BASE_DIR, "magazine", "static", "magazine", "radiance.hub"
    )

    # Collect all the image filenames
    image_data_list = []
    if os.path.exists(static_dir):
        for filename in sorted(os.listdir(static_dir), reverse=True):
            if filename.endswith((".webp", ".jpg", ".jpeg", ".png")):
                image_path = f"magazine/radiance.hub/{filename}"
                datetime_str = filename.split("_UTC")[0]

                try:
                    # Convert the extracted part to a datetime object
                    image_datetime = datetime.strptime(
                        datetime_str, "%Y-%m-%d_%H-%M-%S"
                    )
                    formatted_datetime = image_datetime.strftime(
                        "%B %d, %Y"
                    )
                except ValueError:
                    formatted_datetime = "Unknown Date/Time"

                # Try to find the corresponding caption (same name but with .txt extension)
                filename_without_ext = os.path.splitext(filename)[0]

                # Check for an extra numeric part after the UTC and remove it if present
                if filename_without_ext.endswith("_UTC"):
                    caption_filename = filename_without_ext + ".txt"
                else:
                    caption_filename = '_'.join(filename_without_ext.split('_')[:-1]) + ".txt"

                # Join with the static directory to get the full path
                caption_path = os.path.join(static_dir, caption_filename)

                # Default caption if no caption file exists
                caption = "No caption available"

                # Read caption from the file if it exists
                if os.path.exists(caption_path):
                    with open(caption_path, "r") as caption_file:
                        caption = (
                            caption_file.read().strip()
                        )  # Strip to remove any extra newlines

                # Append the image and its caption to the list
                image_data_list.append(
                    {
                        "image": image_path,
                        "caption": caption,
                        "datetime": formatted_datetime,
                    }
                )
                print(image_data_list)

    return render(
        request, "magazine/radiance.hub.html", {"image_data_list": image_data_list}
    )


def thejaypeedebsoc(request):
    static_dir = os.path.join(
        settings.BASE_DIR, "magazine", "static", "magazine", "thejaypeedebsoc"
    )

    # Collect all the image filenames
    image_data_list = []
    if os.path.exists(static_dir):
        for filename in sorted(os.listdir(static_dir), reverse=True):
            if filename.endswith((".webp", ".jpg", ".jpeg", ".png")):
                image_path = f"magazine/thejaypeedebsoc/{filename}"
                datetime_str = filename.split("_UTC")[0]

                try:
                    # Convert the extracted part to a datetime object
                    image_datetime = datetime.strptime(
                        datetime_str, "%Y-%m-%d_%H-%M-%S"
                    )
                    formatted_datetime = image_datetime.strftime(
                        "%B %d, %Y"
                    )
                except ValueError:
                    formatted_datetime = "Unknown Date/Time"

                # Try to find the corresponding caption (same name but with .txt extension)
                filename_without_ext = os.path.splitext(filename)[0]

                # Check for an extra numeric part after the UTC and remove it if present
                if filename_without_ext.endswith("_UTC"):
                    caption_filename = filename_without_ext + ".txt"
                else:
                    caption_filename = '_'.join(filename_without_ext.split('_')[:-1]) + ".txt"

                # Join with the static directory to get the full path
                caption_path = os.path.join(static_dir, caption_filename)

                # Default caption if no caption file exists
                caption = "No caption available"

                # Read caption from the file if it exists
                if os.path.exists(caption_path):
                    with open(caption_path, "r") as caption_file:
                        caption = (
                            caption_file.read().strip()
                        )  # Strip to remove any extra newlines

                # Append the image and its caption to the list
                image_data_list.append(
                    {
                        "image": image_path,
                        "caption": caption,
                        "datetime": formatted_datetime,
                    }
                )
                print(image_data_list)

    return render(
        request, "magazine/thejaypeedebsoc.html", {"image_data_list": image_data_list}
    )


def thepageturnersociety(request):
    static_dir = os.path.join(
        settings.BASE_DIR, "magazine", "static", "magazine", "thepageturnersociety"
    )

    # Collect all the image filenames
    image_data_list = []
    if os.path.exists(static_dir):
        for filename in sorted(os.listdir(static_dir), reverse=True):
            if filename.endswith((".webp", ".jpg", ".jpeg", ".png")):
                image_path = f"magazine/thepageturnersociety/{filename}"
                datetime_str = filename.split("_UTC")[0]

                try:
                    # Convert the extracted part to a datetime object
                    image_datetime = datetime.strptime(
                        datetime_str, "%Y-%m-%d_%H-%M-%S"
                    )
                    formatted_datetime = image_datetime.strftime(
                        "%B %d, %Y"
                    )
                except ValueError:
                    formatted_datetime = "Unknown Date/Time"

                # Try to find the corresponding caption (same name but with .txt extension)
                filename_without_ext = os.path.splitext(filename)[0]

                # Check for an extra numeric part after the UTC and remove it if present
                if filename_without_ext.endswith("_UTC"):
                    caption_filename = filename_without_ext + ".txt"
                else:
                    caption_filename = '_'.join(filename_without_ext.split('_')[:-1]) + ".txt"

                # Join with the static directory to get the full path
                caption_path = os.path.join(static_dir, caption_filename)

                # Default caption if no caption file exists
                caption = "No caption available"

                # Read caption from the file if it exists
                if os.path.exists(caption_path):
                    with open(caption_path, "r") as caption_file:
                        caption = (
                            caption_file.read().strip()
                        )  # Strip to remove any extra newlines

                # Append the image and its caption to the list
                image_data_list.append(
                    {
                        "image": image_path,
                        "caption": caption,
                        "datetime": formatted_datetime,
                    }
                )
                print(image_data_list)

    return render(
        request,
        "magazine/thepageturnersociety.html",
        {"image_data_list": image_data_list},
    )


def thethespiancircle(request):
    static_dir = os.path.join(
        settings.BASE_DIR, "magazine", "static", "magazine", "thethespiancircle"
    )

    # Collect all the image filenames
    image_data_list = []
    if os.path.exists(static_dir):
        for filename in sorted(os.listdir(static_dir), reverse=True):
            if filename.endswith((".webp", ".jpg", ".jpeg", ".png")):
                image_path = f"magazine/thethespiancircle/{filename}"
                datetime_str = filename.split("_UTC")[0]

                try:
                    # Convert the extracted part to a datetime object
                    image_datetime = datetime.strptime(
                        datetime_str, "%Y-%m-%d_%H-%M-%S"
                    )
                    formatted_datetime = image_datetime.strftime(
                        "%B %d, %Y"
                    )
                except ValueError:
                    formatted_datetime = "Unknown Date/Time"

                # Try to find the corresponding caption (same name but with .txt extension)
                filename_without_ext = os.path.splitext(filename)[0]

                # Check for an extra numeric part after the UTC and remove it if present
                if filename_without_ext.endswith("_UTC"):
                    caption_filename = filename_without_ext + ".txt"
                else:
                    caption_filename = '_'.join(filename_without_ext.split('_')[:-1]) + ".txt"

                # Join with the static directory to get the full path
                caption_path = os.path.join(static_dir, caption_filename)

                # Default caption if no caption file exists
                caption = "No caption available"

                # Read caption from the file if it exists
                if os.path.exists(caption_path):
                    with open(caption_path, "r") as caption_file:
                        caption = (
                            caption_file.read().strip()
                        )  # Strip to remove any extra newlines

                # Append the image and its caption to the list
                image_data_list.append(
                    {
                        "image": image_path,
                        "caption": caption,
                        "datetime": formatted_datetime,
                    }
                )
                print(image_data_list)

    return render(
        request, "magazine/thethespiancircle.html", {"image_data_list": image_data_list}
    )


def ucrjiit(request):
    static_dir = os.path.join(
        settings.BASE_DIR, "magazine", "static", "magazine", "ucrjiit"
    )

    # Collect all the image filenames
    image_data_list = []
    if os.path.exists(static_dir):
        for filename in sorted(os.listdir(static_dir), reverse=True):
            if filename.endswith((".webp", ".jpg", ".jpeg", ".png")):
                image_path = f"magazine/ucrjiit/{filename}"
                datetime_str = filename.split("_UTC")[0]

                try:
                    # Convert the extracted part to a datetime object
                    image_datetime = datetime.strptime(
                        datetime_str, "%Y-%m-%d_%H-%M-%S"
                    )
                    formatted_datetime = image_datetime.strftime(
                        "%B %d, %Y"
                    )
                except ValueError:
                    formatted_datetime = "Unknown Date/Time"

                # Try to find the corresponding caption (same name but with .txt extension)
                filename_without_ext = os.path.splitext(filename)[0]

                # Check for an extra numeric part after the UTC and remove it if present
                if filename_without_ext.endswith("_UTC"):
                    caption_filename = filename_without_ext + ".txt"
                else:
                    caption_filename = '_'.join(filename_without_ext.split('_')[:-1]) + ".txt"

                # Join with the static directory to get the full path
                caption_path = os.path.join(static_dir, caption_filename)

                # Default caption if no caption file exists
                caption = "No caption available"

                # Read caption from the file if it exists
                if os.path.exists(caption_path):
                    with open(caption_path, "r") as caption_file:
                        caption = (
                            caption_file.read().strip()
                        )  # Strip to remove any extra newlines

                # Append the image and its caption to the list
                image_data_list.append(
                    {
                        "image": image_path,
                        "caption": caption,
                        "datetime": formatted_datetime,
                    }
                )
                print(image_data_list)

    return render(
        request, "magazine/ucrjiit.html", {"image_data_list": image_data_list}
    )
