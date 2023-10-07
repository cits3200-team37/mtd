/**
 * @return {string} tag for the latest release version
 *
 */
import axios from "axios";
export default async function getTag() {
  const url =
    "https://api.github.com/repos/cits3200-team37/mtd/releases/latest";
  const { data, status } = await axios.get(url);
  if (status == 200) return data;
}
