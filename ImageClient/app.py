import click
from utils import get_server_image, download_image


@click.command()
@click.argument("name", default="img01")
@click.option("--download", "-d", is_flag=True)
def main(name, download):
    click.echo(f"Image name: {name}")
    server_img = get_server_image(img_name=name)

    if not server_img:
        click.echo("Image not found in server")
        return

    click.echo(f"Image html: {server_img.html}")
    
    if download:
        msg = "Image downloaded successfully"
        if not download_image(name):
            msg = "Error downloading image"
        click.echo(msg)


if __name__ == '__main__':
    main()