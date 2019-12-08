using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace ImageServer.Controllers
{
    public class HomeController : Controller
    {

        public ActionResult Index()
        {
            return View();
        }

        public ActionResult Images(string name="img01")
        {
            validateImage(name);

            string folderPath = "/Content/images";
            string imageExt = "jpg";
            string imagePath = $"{folderPath}/{name}.{imageExt}";
 
            ViewBag.ImageName = name;
            ViewBag.ImagePath = imagePath;

            return View();
        }

        void validateImage(string name)
        {
            // Harcoded name of images in Content/images folder
            string[] imagesNames = new string[] { "img01", "img02", "img03", "img04" };

            if (!imagesNames.Contains(name))
            {
                throw new HttpException(404, $"Image {name} not found");
            }
        }

    }
}