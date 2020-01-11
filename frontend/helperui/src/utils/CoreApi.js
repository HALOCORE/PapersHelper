import axios from 'axios';

const apiBase = "http://localhost:8000/";
export default class CoreApi {
  static reloads() {
    return axios.get(apiBase + "reloads");
  }
  static filetree_get() {
    return axios.get(apiBase + "filetree").catch(
      () => console.error("# filetree_get failed."));
  }
  static filetree_update() {
    return axios.get(apiBase + "filetree/update").catch(
      () => console.error("# filetree_update failed."));
  }
  static file_search() {
    return axios.get(apiBase + "file/search").catch(
      () => console.error("# file_search failed."));
  }
  static file_summary_get(fileid) {
    return axios.get(apiBase + "file/summary?fileid=" + fileid).catch(
      () => console.error("# file_summary_get failed."));
  }
  static file_refs_get(fileid) {
    return axios.get(apiBase + "file/refs?fileid=" + fileid).catch(
      () => console.error("# file_refs_get failed."));
  }
  static file_fulltxt_get(fileid) {
    return axios.get(apiBase + "file/fulltxt?fileid=" + fileid).catch(
      () => console.error("# file_fulltxt_get failed."));
  }
}