from conan.packager import ConanMultiPackager

if __name__ == "__main__":
    builder = ConanMultiPackager()
    builder.add_common_builds(reference="llvm/9.0.0")
    # builder.add_common_builds(reference="llvm/9.0.0")
    builder.run()
