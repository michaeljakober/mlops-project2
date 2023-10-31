import sys
from model_training import train
import time

if __name__ == '__main__':
    # Get the command-line arguments as a list
    command_line_args = sys.argv

    # Find the index of the different arguments
    if '--lr' in command_line_args:
        lr_index = command_line_args.index('--lr')
        learning_rate = float(command_line_args[lr_index + 1])
    else:
        learning_rate = 2e-5  # Default value

    if '--wd' in command_line_args:
        wd_index = command_line_args.index('--wd')
        weight_decay = float(command_line_args[wd_index + 1])
    else:
        weight_decay = 1e-2  # Default value

    if '--warmup-steps' in command_line_args:
        warmup_steps_index = command_line_args.index('--warmup-steps')
        warmup_steps = float(command_line_args[warmup_steps_index + 1])
    else:
        warmup_steps = 100  # Default value

    # Use the retrieved values
    print(f'Learning rate : {learning_rate}')
    print(f'Weight decay  : {weight_decay}')
    print(f'Warmup steps  : {warmup_steps}')

    start_time = time.time()

    print("Starting Training...")
    train(learning_rate, weight_decay, warmup_steps)

    print(f'Finished Training in {time.time() - start_time:.2f} Seconds')

