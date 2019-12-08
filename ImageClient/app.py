import click
from utils import ImageClient


@click.command()
@click.argument("name", default="img01")
@click.option("--download", "-d", is_flag=True)
def main(name, download):
    server_img = ImageClient.get_server_image(img_name=name)
    if not server_img:
        click.echo(f"Image {name} not found in server")
        return

    click.echo(f"Image name: {name}")
    click.echo(f"Image html: {server_img.html}")

    if download:
        ImageClient.download_image(name)
        click.echo("Image downloaded successfully")


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"Ha ocurrido un error: \n{e}")
