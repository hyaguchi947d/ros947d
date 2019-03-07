# ros947d_darknet

## Author

Hiroaki Yaguchi (h-yaguchi@947d-tech.co.jp)

## Abstract

This is a utility package for darknet_ros.

## nodes

### result_viewer.py

result_viewer.py shows results of darknet on the input image.

```
$ rosrun ros947d_darknet result_viewer.py image:=<input image topic>
```

### compressed_result_viewer.py

compressed_result_viewer.py shows results of darknet on the COMPRESSED input image.

```
$ rosrun ros947d_darknet compressed_result_viewer.py image:=<compressed input image topic>
```
