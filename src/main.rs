use fs_extra::dir;
use opencv::prelude::*;
use std::time::Instant;
use xcap::Window;

fn normalized(filename: &str) -> String {
    filename.replace(['|', '\\', ':', '/'], "")
}

fn get_window(export_image: bool) {
    let start = Instant::now();
    let windows = Window::all().unwrap();

    dir::create_all("target/windows", true).unwrap();

    let mut i = 0;
    for window in &windows {
        if window.is_minimized().unwrap() || window.title().unwrap() != "Nyan Cat: Lost In Space" {
            //I only really care about Nyan cat :3
            if &window.title().unwrap() == &windows[i].title().unwrap() {
                println!("Sowwy myan I couldn't find nyan cat anywhere!!");
            }
            continue;
        }
        println!(
            //formatting image
            "Window: {:?} {:?} {:?}",
            window.title().unwrap(), //window title
            (
                //window dimensions
                window.x().unwrap(),
                window.y().unwrap(),
                window.width().unwrap(),
                window.height().unwrap()
            ),
            (
                window.is_minimized().unwrap(),
                window.is_maximized().unwrap()
            )
        );

        let image = window.capture_image().unwrap();
        if export_image == true {
            image
                .save(format!(
                    "target/windows/window-{}-{}.png",
                    i,
                    normalized(&window.title().unwrap())
                ))
                .unwrap();
        }

        i += 1;
        println!("It took {:?}", start.elapsed());
        //I wanna break here so if we have like a list [blah blah nyan_cat blah blah], why search blah and blah after
        //we find nyan cat because like I dont really care about them.
        break; // should maybe probably work(?) 
    }
}

fn main() {
    get_window(true);
}
