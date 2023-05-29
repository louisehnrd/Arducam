def zoom_picture(zoom_factor):
    arducam.start()

    size = arducam.capture_metadata()['ScalerCrop'][zoom_factor:]
    full_res = arducam.camera_properties['PixelArraySize']
    #print(full_res)

    #zoom progressif
    for _ in range(20):
        # This syncs us to the arrival of a new camera frame:
        arducam.capture_metadata()

        size = [int(s * 0.95) for s in size]
        offset = [(r - s) // 2 for r, s in zip(full_res, size)]
        arducam.set_controls({"ScalerCrop": offset + size})

    #chemin du fichier sortant
    timestamp = time.strftime('%Y.%m.%d-%H:%M:%S')
    filename = 'picture_{}.jpg'.format(timestamp)
    output_file = os.path.join(os.path.expanduser("~"), "Pictures", filename)

    #prend un photo
    arducam.capture_file(output_file)
    
    arducam.close()
