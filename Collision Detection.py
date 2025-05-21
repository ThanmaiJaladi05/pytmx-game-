def check_collision(player, obstacles):
    for obstacle in obstacles:
        if player.rect.colliderect(obstacle.rect):
            return True
    return False
