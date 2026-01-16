use fs_extra::dir;
use opencv::prelude::*; //It's yelling at me for not using it but I think we need it anyways.
use std::path::Path;
use std::time::Instant;
use xcap::Window;

fn normalized(filename: &str) -> String {
    //Like fricking formats your strings so that we can use it in xcap :3
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
            if window.title().unwrap() == windows[windows.len() - 1].title().unwrap() {
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
                //is the window minimized or maximize (both can be false btw)
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
        //we find nyan cat because like I don't really care about them.
        break; // should maybe probably work(?) 
    }
}

/*
fn _find_objects() {
    //Guess who uses YOLO??? meeeee!!!
}
    */

fn main() {
    //Shhhh
    let is_present: bool;
    is_present = Path::new("../coconut.jpeg").exists();
    // if is_present == false {
    //     panic!()
    // }

    get_window(true);
}
