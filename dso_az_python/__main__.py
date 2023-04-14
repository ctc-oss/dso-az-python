from dso_az_python.utils import azure_vm
import argparse


def main(args):
    if args.start:
        azure_vm.start(args.vm)
    elif args.stop:
        azure_vm.stop(args.vm)
    elif args.deallocate:
        azure_vm.deallocate(args.vm)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--vm", type=str, required=True, help="Name of VM to use")
    parser.add_argument("--start", default=False, action="store_true", help="Start VM")
    parser.add_argument("--stop", default=False, action="store_true", help="Stop VM")
    parser.add_argument(
        "--deallocate", default=False, action="store_true", help="Deallocate VM"
    )
    args = parser.parse_args()
    main(args)
