/* Copyright (c) 2012-2015 LevelDOWN contributors
 * See list at <https://github.com/rvagg/node-leveldown#contributing>
 * MIT License <https://github.com/rvagg/node-leveldown/blob/master/LICENSE.md>
 */

#include <node.h>
#include <node_buffer.h>

#include "database.h"
#include "snapshot.h"

namespace leveldown {


static v8::Persistent<v8::FunctionTemplate> snapshot_constructor;

Snapshot::Snapshot (
    Database* database
) : database(database)
  , dbSnapshot(database->NewSnapshot())
{
  Nan::HandleScope scope;

  v8::Local<v8::Object> obj = Nan::New<v8::Object>();
  // NanAssignPersistent(persistentHandle, obj);
  persistentHandle.Reset(v8::Isolate::GetCurrent(), obj);
}

Snapshot::~Snapshot () {
  database->ReleaseSnapshot(dbSnapshot); // TODO: is this safe?
  if (!persistentHandle.IsEmpty())
    // NanDisposePersistent(persistentHandle);
    persistentHandle.Reset();
}

void Snapshot::Init () {
  v8::Local<v8::FunctionTemplate> tpl =
      Nan::New<v8::FunctionTemplate>(Snapshot::New);
  // NanAssignPersistent(snapshot_constructor, tpl);
  snapshot_constructor.Reset(v8::Isolate::GetCurrent(), tpl);
  tpl->SetClassName(Nan::New("Snapshot").ToLocalChecked());
  tpl->InstanceTemplate()->SetInternalFieldCount(1);
}

v8::Local<v8::Object> Snapshot::NewInstance (
        v8::Local<v8::Object> database
    ) {
//  NanEscapableScope();
  Nan::EscapableHandleScope scope;

  v8::Local<v8::Object> instance;
  v8::Local<v8::FunctionTemplate> constructorHandle =
      Nan::New<v8::FunctionTemplate>(snapshot_constructor);

  v8::Handle<v8::Value> argv[1] = { database };
  instance = constructorHandle->GetFunction()->NewInstance(1, argv);

  return scope.Escape(instance);
}

bool Snapshot::HasInstance (
        v8::Handle<v8::Value> value
    ) {
        return Nan::New(snapshot_constructor)->HasInstance(value);
}

NAN_METHOD(Snapshot::New) {
  Nan::HandleScope scope;

  Database* database = node::ObjectWrap::Unwrap<Database>(info[0]->ToObject());

  Snapshot* snapshot = new Snapshot(
      database
  );
  snapshot->Wrap(info.This());
  info.GetReturnValue().Set(info.This());
}


} // namespace leveldown
