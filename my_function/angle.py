def goto_angle( current_angle, dest_angle, speed):
    result_angle_list = []
    finish = False
    while finish == False:
        if speed >= 0:
            if dest_angle > current_angle:
                current_angle += speed
            elif dest_angle <= current_angle:
                current_angle = dest_angle
                finish = True
        
        if speed < 0:
            if dest_angle < current_angle:
                current_angle += speed
                finish = False
            elif dest_angle >= current_angle:
                current_angle = dest_angle
                finish = True
        print(current_angle)
        result_angle_list.append(current_angle)
    
    return result_angle_list

def get_angle_list(current_angle, angle_list, speed):
    result_angle_list = [current_angle]
    for i in angle_list:
        if result_angle_list[-1] < i:
            result_angle_list = result_angle_list + goto_angle(result_angle_list[-1] ,i, speed)
        else:
            result_angle_list = result_angle_list + goto_angle(result_angle_list[-1] ,i, -speed)

    return result_angle_list


