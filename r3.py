from dotenv import load_dotenv
import logging

import clitools
import aifunctions
import processing

def main() -> None:
    parser = clitools.build_parser()
    args = parser.parse_args()

    logging.basicConfig(level = args.loglevel)
    logging.debug(f"Args: {args}")

    for f in args.input:
        logging.info(f"Transcribing {f}")

        transcript = aifunctions.transcribe_audio(f)
        points = aifunctions.refine_keypoints(transcript)
        
        processing.append_records(f, points)
    
    output = processing.process_output(processing.get_records(), format_type = args.output_format)

    return output

if __name__ == "__main__":
    print(main())