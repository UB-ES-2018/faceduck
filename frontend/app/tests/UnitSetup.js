class LocalStorageMock {
  constructor() {
    this.store = {};
  }

  clear() {
    this.store = {};
  }

  getItem(key) {
    return this.store[key] || null;
  }

  setItem(key, value) {
    this.store[key] = value.toString();
  }

  removeItem(key) {
    delete this.store[key];
  }
};

global.localStorage = new LocalStorageMock;

/**
 * Mock Promises: since we only need to avoid any API calls,
 * this object has the required methods and never does anything
 */
var fakePromise = {
  then: () => { return { ...fakePromise } },
  catch: () => { return { ...fakePromise } }
}

global.fetch = () => { return { ...fakePromise } };

localStorage.setItem("user", JSON.stringify({
  "id": "90ada2f2-1b5d-4319-9c55-77ea566015e4",
  "username": "john",
  "name": "John",
  "surname": "Appleseed",
  "email": "john@apple.com", 
  "gender": "other"
}));

