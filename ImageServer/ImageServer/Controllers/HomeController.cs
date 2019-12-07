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
            string imageName = $"{name}";
            string folterPath = "/Content/images/";
            string imagePath = $"{folterPath}{imageName}.jpg";
            ViewBag.ImageName = imageName;
            ViewBag.ImagePath = imagePath;

            return View();
        }

    }
}